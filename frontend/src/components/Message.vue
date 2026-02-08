<script setup>
import { ref, watch, nextTick, onMounted, computed } from 'vue'; 
import { useConversationStore } from '@/stores/conversationStore';
import { useCharacterStore } from '@/stores/characterStore'

const characterStore = useCharacterStore();
const conversationStore = useConversationStore();
const selectedCharacter = computed(() => characterStore.selectedCharacter);

const history = computed(() => conversationStore.history);
const currentChannel = computed(() => selectedCharacter.value?.name ?? "Arthur"); // hardcodé
const filteredHistory = computed(() => {
  if (!currentChannel.value) return history.value;
  return history.value.filter(m => m.channel === currentChannel.value);
});

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

const lastMessage = computed(() => {
  const arr = filteredHistory.value;
  return arr && arr.length ? arr[arr.length - 1] : null;
});


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
    conversationStore.fetchHistory('A',newCharacter.name).then(() => {
      scrollToBottom();
    });
  } else {
    conversationStore.clearConversation();
  }
}, { immediate: true }); 

onMounted(() => {
  conversationStore.fetchHistory('A', 'Arthur').then(() => {
    scrollToBottom();
  });//TODO : afficher la réponse du joueur qu'apres qu'il ait répondu (duh)
});
</script>

<template>
<v-main>    
  <v-container fluid class="fill-height pa-0">
    <div class="chat-container d-flex flex-column fill-height">
      <div class="messages-list flex-grow-1" ref="messagesContainerRef">
        <v-list lines="three" class="bg-transparent ">
          <v-list-item v-for="message in filteredHistory" :key="message.id" class="message-item"> 
            <template v-slot:prepend>
              <v-avatar color="primary" :image="characters[message.character]?.picture">
              </v-avatar>
            </template>
            <v-list-item-title class="font-weight-bold">
              {{ message.character }}
              <span class="text-caption text-grey ml-2">10h23</span>
            </v-list-item-title>
            <v-list-item-subtitle class="message-text">
              {{ message.content }}
            </v-list-item-subtitle>         
          </v-list-item>
        </v-list>
      </div>
    </div>
      <div v-if="lastMessage && lastMessage.choices && lastMessage.choices.length" class="bottom-choices pa-2">
        <v-row justify="center">
          <v-btn v-for="choice in lastMessage.choices" :key="choice.id" class="ma-1" @click="conversationStore.send_choice('A', lastMessage.channel ?? currentChannel.value, choice.id,choice.text)">
              {{ choice.text }}
          </v-btn>
        </v-row>
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

  