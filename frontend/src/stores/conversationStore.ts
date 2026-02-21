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
    isFinished: false,
    profilePicture: "",
  }),
  actions: {
    async fetchHistory(channel_name: string) {
      this.isLoading = true;
      try {
        const response = await axios.get(`/api/history/${channel_name}`);
        this.history = response.data;
      } catch (error) {
        console.error("Erreur lors du chargement de l'historique:", error);
      } finally {
        this.isLoading = false;
      }
    },
    clearConversation() {
      this.history = [];
      this.isFinished = false;
    },
    async new_message(channel_name: string) {
      this.isLoading = true;
      this.isFinished = false;
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
        const response = await axios.get(`/api/send`);
        const payload = response.data;
        const content: string =
          typeof payload === 'string'
            ? payload
            : (payload?.content ?? "");

        const character = (payload && payload.character) ? payload.character : 'System';
        const choices = payload?.choices ?? null;
        const channel = payload?.channel ?? null;

        const finalMsg: Message = {
          id: Date.now(),
          character,
          content,
          choices,
          channel,
    
        };
        //TODO notifications
        
        const idx = this.history.findIndex(m => m.id === tempId);

        if (character === 'player') {
          if (idx !== -1) {
            this.history.splice(idx, 1);
          }
          return finalMsg; 
        } 
    
        if (idx !== -1) {
          this.history.splice(idx, 1, finalMsg);
        } else {
          this.history.push(finalMsg);
        }

        return finalMsg;

      } catch (error: any) {
        const idx = this.history.findIndex(m => m.id === tempId);
        if (idx !== -1) this.history.splice(idx, 1);
        if (error.response && error.response.status === 404) {
          this.isFinished = true;
        }
        throw error;
        
      } finally {
        this.isLoading = false;
      }
    },
    async reset_history(){
      this.isLoading = true;
      try {
        await axios.get(`/api/reset`);
        this.history = [];
      } catch (error) {
        console.error("Erreur lors de la réinitialisation de l'historique:", error);
      } finally {
        this.isLoading = false;
      }
    },
    async send_choice(channel_name: string, answer : number, choice_text?: string){
      this.isLoading=true;
      const playerMsg: Message = {//peut etre totalement inutile, a voir.
        id: Date.now(),
        character: 'Player', 
        content: choice_text ?? String(answer),
        choices: null,
        channel: channel_name,
      };
      this.history.push(playerMsg);
      try{
        await axios.get(`/api/recv/${channel_name}/${answer}`);
        await this.fetchHistory(channel_name)
      }catch(error){
        const idx = this.history.findIndex(m => m.id === playerMsg.id);
        if (idx !== -1) this.history.splice(idx, 1);
        throw error;
      }finally{
        this.isLoading=false;
      }
    },
    async end_conversation(){
      this.isLoading=true;
      try{
        await axios.get(`/api/end`);
        this.isFinished = false;
      }catch(error){
        console.error("Erreur lors de la fin de la conversation:", error);
      }finally{
        this.isLoading=false;
      }
    },
    async fetchProfilePicture(){
        const apiProfilePicture = await axios.get('/api/profile_picture')
        this.profilePicture=apiProfilePicture.data[0];
    }
  }

});