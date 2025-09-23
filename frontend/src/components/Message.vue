<script setup>
import { ref, watch, nextTick, onMounted, computed } from 'vue'; 
import { useConversationStore } from '@/stores/conversationStore';
import { useCharacterStore } from '@/stores/characterStore'

const characterStore = useCharacterStore();
const conversationStore = useConversationStore();
const selectedCharacter = computed(() => characterStore.selectedCharacter);

const history = computed(() => conversationStore.history);
const characters = computed(() => characterStore.characterMap);
const messagesContainerRef = ref<HTMLDivElement | null>(null); 
const scrollToBottom = () => {
  const container = messagesContainerRef.value;
  if (container) {
    container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
  }
  if (characterStore.characters.length === 0) {
    characterStore.fetchCharacters();
  }
};

watch(history, () => {
  nextTick(() => {
    scrollToBottom();
  });
}, { deep: true });

watch(selectedCharacter, (newCharacter, oldCharacter) => {
  if (newCharacter?.name === oldCharacter?.name) {
    return;
  }
  
  if (newCharacter) {
    console.log(`Le personnage sélectionné a changé pour : ${newCharacter.name}. Chargement de son historique...`);
    conversationStore.fetchHistory('B',newCharacter.name).then(() => {
      scrollToBottom();
    });
  } else {
    conversationStore.clearConversation();
  }
}, { immediate: true }); 

onMounted(() => {
  conversationStore.fetchHistory('B', 'Arthur').then(() => {
    scrollToBottom();
  });
});
</script>

<template>
<v-main>    
  <v-container fluid class="fill-height pa-0">
    <div class="chat-container d-flex flex-column fill-height">
      <div class="messages-list flex-grow-1" ref="messagesContainerRef">
        <v-list lines="three" class="bg-transparent ">
          <v-list-item v-for="message in history" :key="message.id" class="message-item">
            <template v-slot:prepend>
              <v-avatar color="primary" :image="characters[message.character]?.picture">
              </v-avatar>
            </template>
            <v-list-item-title class="font-weight-bold">
              {{ message.character }}
              <span class="text-caption text-grey ml-2">10h23</span>
            </v-list-item-title>
            <v-list-item-subtitle class="message-text" v-if="message.picture_or_text === 'text'">
              {{ message.content }}
            </v-list-item-subtitle>
            <v-list-item-subtitle class="message-text" v-if="message.picture_or_text === 'picture'">
              {{ message.content }}
            </v-list-item-subtitle>            
          </v-list-item>
        </v-list>
      </div>

      <div class="message-input-area pa-2">
        <v-text-field
          label="Écrire un message..."
          variant="solo"
          hide-details
          append-inner-icon="mdi-send"
        ></v-text-field>
      </div>
    </div>
  </v-container>
</v-main>
</template>

    
<style scoped>
.chat-container {
  width: 100%;
}

.dark-main-content{
    width: 100%;
    
}
.messages-list {
  overflow-y: auto;
  height: 0;
  flex-grow: 1;

}


.message-item {
  margin-bottom: 12px;
  
}


.bg-transparent :hover{
    background-color: rgba(255, 255, 255, 0.1) !important;
}

.message-item :hover{
    background-color: rgba(255, 255, 255, 0) !important;
}


.message-text {
  white-space: normal;
  word-wrap: break-word;
}

.message-input-area {
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
</style>

  