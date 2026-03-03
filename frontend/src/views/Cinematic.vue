<script setup>
import { useConversationStore } from '@/stores/conversationStore';
import { onMounted, onUnmounted ,computed} from 'vue';
const conversationStore = useConversationStore();
const messages = computed(() => conversationStore.history);


const handleKeyPress = (event) => {
  if (event.key === " " || event.code === "Space") {
    event.preventDefault();
    conversationStore.new_message()
  }
};

onMounted(() => {
  window.addEventListener('keydown', handleKeyPress);
  conversationStore.getBackground();
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyPress);
});

const lastMessage = computed(() => {
  const arr = messages.value;
  return arr && arr.length ? arr[arr.length - 1] : null;
});

const currentBackground = computed(() => {
  const cinematicMessages = messages.value.filter(m => m.character === 'Cinematic');
  if (cinematicMessages.length > 0) {
    const Background = cinematicMessages[cinematicMessages.length - 1].content;
    return Background
  }
  else{
    return conversationStore.background
  }
});

</script>



<template>
<v-img :src="currentBackground" cover fill-width>
  <div v-for="message in messages">
    <div v-if="message.character==='Cinematic'">
      {{background=message.content.split(1)}}
    </div>
    <div v-else>
      {{message.content}}
      {{message.character }}
    </div>
  </div>
  <div v-if="lastMessage && lastMessage.choices && lastMessage.choices.length" class="pa-2">
    <v-row justify="center">
      <v-btn v-for="choice in lastMessage.choices" :key="choice.id" class="ma-1" @click="conversationStore.send_choice(lastMessage.channel ?? currentChannel.value, choice.id,choice.points , choice.text)">
        {{ choice.text }}
      </v-btn>
    </v-row>
  </div>
  <v-btn @click="conversationStore.reset_history()">
  reset
  </v-btn>
</v-img>
</template>