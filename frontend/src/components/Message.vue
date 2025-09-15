<script setup>
import { ref, watch, nextTick, onMounted } from 'vue';
const pfpUrl = new URL('../assets/Pfp/zouaient.jpg', import.meta.url).href;
const messages = ref([
  { 
    id: 1, 
    author: 'A', 
    avatarUrl: pfpUrl, 
    text: 'QUOICOUUUUUUUUUUUU',
    timestamp: '10:30' 
  },
  { 
    id: 2, 
    author: 'B', 
    avatarUrl: pfpUrl, 
    text: 'waaaaaaahahahaaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahhahwaabaaahh',
    timestamp: '10:31'
  },
  { 
    id: 3, 
    author: 'C', 
    avatarUrl: pfpUrl, 
    text: 'Carrément',
    timestamp: '10:32'
  },
  { 
    id: 4, 
    author: 'D', 
    avatarUrl: pfpUrl, 
    text: 'Bonjour à tous.',
    timestamp: '10:35'
  },
  { 
    id: 5, 
    author: 'A', 
    avatarUrl: pfpUrl, 
    text: 'QUOICOUUUUUUUUUUUU',
    timestamp: '10:30' 
  },
  { 
    id: 6, 
    author: 'B', 
    avatarUrl: pfpUrl, 
    text: 'waaaaaaahahahaaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahaaaaahahahahahwaabaaahhahwaabaaahh',
    timestamp: '10:31'
  },
  { 
    id: 7, 
    author: 'C', 
    avatarUrl: pfpUrl, 
    text: 'Carrément',
    timestamp: '10:32'
  },
  { 
    id: 8, 
    author: 'D', 
    avatarUrl: pfpUrl, 
    text: 'Bonjour à tous.',
    timestamp: '10:35'
  },
  { 
    id: 9, 
    author: 'C', 
    avatarUrl: pfpUrl, 
    text: 'Carrément',
    timestamp: '10:32'
  },
  { 
    id: 10, 
    author: 'D', 
    avatarUrl: pfpUrl, 
    text: 'Bonjour à tous.',
    timestamp: '10:35'
  },
  { 
    id: 11, 
    author: 'FINAL', 
    avatarUrl: pfpUrl, 
    text: 'Yataaaa !!!',
    timestamp: '10:35'
  },
]);

const messagesContainerRef = ref(null);

const scrollToBottom = () => {
  const container = messagesContainerRef.value;
  if (container) {
    container.scrollTop = container.scrollHeight;
  }
};

watch(messages, () => {
  nextTick(() => {
    scrollToBottom();
  });
}, { deep: true }); 

onMounted(() => {
  scrollToBottom();
});
</script>

<template>    
<v-main class="dark-main-content" >
  <v-container fluid class="fill-height pa-0">
    <div class="chat-container d-flex flex-column fill-height">
      <div class="messages-list flex-grow-1" ref="messagesContainerRef">
        <v-list lines="three" class="bg-transparent ">
          <v-list-item v-for="message in messages" :key="message.id" class="message-item">
            <template v-slot:prepend>
              <v-avatar color="primary">
                <v-img :src="message.avatarUrl" :alt="message.author">
                </v-img>
              </v-avatar>
            </template>

            <v-list-item-title class="font-weight-bold">
              {{ message.author }}
              <span class="text-caption text-grey ml-2">{{ message.timestamp }}</span>
            </v-list-item-title>

            <v-list-item-subtitle class="message-text">
              {{ message.text }}
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
  padding: 16px;
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

  