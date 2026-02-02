import { defineStore } from 'pinia'
import axios from 'axios'

export interface Choice {
  id: number;
  text: string;
}

export interface Message {
  id: number;
  character: string;
  picture_or_text: 'text' | 'image' | null;
  content: string | null;
  choices: Choice[] | null;
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
    playerMadeChoice(choice: Choice) {
      console.log(`Le joueur a choisi : "${choice.text}" (ID: ${choice.id})`);
    },
    clearConversation() {
      this.history = [];
    },
    async new_message(player_name: string, channel_name: string) {
      console.log("New message requested");
      this.isLoading = true;
      try{
        const response = await axios.get(`/api/send/${player_name}`);
        return response.data;
        }  catch (error) {
        console.error("Erreur lors de la demande de nouveau message:", error);
        } finally {
        this.isLoading = false;
      }
    }
  }
});