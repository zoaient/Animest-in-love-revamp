// src/stores/conversationStore.ts
import { defineStore } from 'pinia'
import axios from 'axios'

export interface Message {
  id: number
  author: string
  text: string
  avatarUrl?: string 
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
    async fetchConversation(characterId: number) {
      this.isLoading = true
      this.error = null
      this.messages = [] 
      try {
        const response = await axios.get(`/api/conversations/${characterId}`)
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