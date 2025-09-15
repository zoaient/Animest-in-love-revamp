// src/stores/conversationStore.ts
import { defineStore } from 'pinia'
import axios from 'axios' // On aura besoin d'un client HTTP comme Axios

export interface Message {
  id: number
  author: string
  text: string
  avatarUrl?: string // L'avatar est optionnel ici
}

interface ConversationState {
  messages: Message[]
  isLoading: boolean
  error: string | null
}

export const useConversationStore = defineStore('conversation', {
  state: (): ConversationState => ({
    messages: [],
    isLoading: false,
    error: null,
  }),
  actions: {
    // L'action clé qui va appeler notre backend
    async fetchConversation(characterId: number) {
      this.isLoading = true
      this.error = null
      this.messages = [] // On vide la conversation précédente

      try {
        // C'est ici que la magie opère !
        // On fait un appel à notre future API backend.
        const response = await axios.get(`/api/conversations/${characterId}`)
        
        // On met à jour l'état avec les données reçues du backend
        this.messages = response.data
      } catch (err) {
        this.error = `Impossible de charger la conversation pour le personnage ${characterId}.`
        console.error(err)
      } finally {
        this.isLoading = false
      }
    },
    
    clearConversation() {
      this.messages = [];
    }
  },
})