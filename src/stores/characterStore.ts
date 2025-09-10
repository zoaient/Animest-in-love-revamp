import { defineStore } from 'pinia'
import characterData from '../data/Characters.json' assert { type: 'json' };

export interface Character {
  id: number
  name: string
  color: string
  picture: string
  resolvedPictureUrl?: string
}

interface CharacterState {
  characters: Character[]
  isLoading: boolean
  error: string | null
}

export const useCharacterStore = defineStore('characters', {
  state: (): CharacterState => ({
    characters: [], 
    isLoading: false,
    error: null,
  }),
  getters: {
    getCharacterById: (state) => (id: number) => {
      return state.characters.find(char => char.id === id)
    },
  },
  actions: {
    async fetchCharacters() {
      this.isLoading = true
      this.error = null
      try {
        await new Promise(resolve => setTimeout(resolve, 1000));
        this.characters = characterData as Character[];
        console.log('Personnages chargés dans le store !', this.characters);
      } catch (err) {
        this.error = 'Erreur lors du chargement des personnages.'
        console.error(err)
      } finally {
        this.isLoading = false
      }
    },
  },
})