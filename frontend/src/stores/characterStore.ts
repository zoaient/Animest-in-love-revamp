import { defineStore } from 'pinia'
import { useConversationStore } from './conversationStore' 
import axios from 'axios'

export interface Character {
  name: string
  color: string
  picture: string
  resolvedPictureUrl?: string
}

interface CharacterState {
  characters: Character[]
  isLoading: boolean
  error: string | null
  selectedCharacterName: string | null
}

export const useCharacterStore = defineStore('characters', {
  state: (): CharacterState => ({
    characters: [], 
    isLoading: false,
    error: null,
    selectedCharacterName: null,
  }),
  getters: {
    getCharacterByName: (state) => (id: string) => {
      return state.characters.find(char => char.name === id)
    },
    selectedCharacter(state): Character | null {
      if (state.selectedCharacterName === null) {
        return null;
      }
      return state.characters.find(char => char.name === state.selectedCharacterName) || null;
    },
    characterMap(state): { [name: string]: Character } {
      return state.characters.reduce((map, char) => {
        map[char.name] = char;
        return map;
      }, {} as { [name: string]: Character });
    },
  },
  actions: {
    async fetchCharacters() {
      this.isLoading = true
      this.error = null
      try {
        //pnjs
        const response = await axios.get('/api/characters')
        const fetchedCharacters = response.data as Character[];
        this.characters = fetchedCharacters.map(char => ({
          ...char,
          resolvedPictureUrl: new URL(`../assets/${char.picture}`, import.meta.url).href //TODO simplifier
        }));
      } catch (err) {
        console.error(err)
      } finally {
        this.isLoading = false
      }
    },
    selectCharacter(character: Character | null) {
      console.log(character)
      if (character) {
        this.selectedCharacterName = character.name;
        console.log(`Personnage sélectionné : ${character.name}`);
      } else {
        this.selectedCharacterName = null;
        console.log('Personnage désélectionné.');
      }
    }
  }
})