import { defineStore } from 'pinia'
import axios from 'axios'

export interface Choice {
  id: number;
  text: string;
}

export interface Message {
  id: number;
  character: string;
  content: string | null;
  choices: Choice[] | null;
  channel?: string;
}


export const useConversationStore = defineStore('conversation', {
  state: () => ({
    history: [] as Message[],
    isLoading: false,
  }),
  actions: {
    async fetchHistory(player_name: string, channel_name: string) {
      this.isLoading = true;
      try {
        const response = await axios.get(`/api/history/${player_name}/${channel_name}`);
        this.history = response.data;
      } catch (error) {
        console.error("Erreur lors du chargement de l'historique:", error);
      } finally {
        this.isLoading = false;
      }
    },
    playerMadeChoice(choice: Choice) { //faudra virer ça un jour
      console.log(`Le joueur a choisi : "${choice.text}" (ID: ${choice.id})`);
    },
    clearConversation() {
      this.history = [];
    },
    async new_message(player_name: string, channel_name: string) {
      this.isLoading = true;
      const tempId = Date.now();
      const tempMsg: Message = {
        id: tempId,
        character: 'System',
        content: 'En attente...',
        choices: null,
        channel: channel_name,
      };
      this.history.push(tempMsg);

      try {
        const response = await axios.get(`/api/send/${player_name}`);
        const payload = response.data;
        const content: string =
          typeof payload === 'string'
            ? payload
            : (payload?.content ?? String(payload ?? ''));

        const character = (payload && payload.character) ? payload.character : 'System';
        const choices = payload?.choices ?? null;

        const finalMsg: Message = {
          id: Date.now(),
          character,
          content,
          choices,
          channel: payload?.channel ?? channel_name,
    
        };
        //TODO gérer gerer le cas player et le systeme de notifications 

        const idx = this.history.findIndex(m => m.id === tempId);
        if (idx !== -1) {
          this.history.splice(idx, 1, finalMsg);
        } else {
          this.history.push(finalMsg);
        }

        return finalMsg;

      } catch (error) {
        const idx = this.history.findIndex(m => m.id === tempId);
        if (idx !== -1) this.history.splice(idx, 1);
        throw error;
      } finally {
        this.isLoading = false;
      }
    }
  }
});