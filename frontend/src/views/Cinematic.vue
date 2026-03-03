<script setup>
import { useCharacterStore } from '@/stores/characterStore';
import { useConversationStore } from '@/stores/conversationStore';
import { onMounted, onUnmounted ,computed} from 'vue';
const conversationStore = useConversationStore();
const characterStore = useCharacterStore();
const messages = computed(() => conversationStore.history);
const background = computed (() => conversationStore.background);


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


</script>



<template>
<v-img :src="background" cover max-width="300">
{{background}}
</v-img>
<div v-for="message in messages">
    {{message.content}}

</div>
<v-btn @click="conversationStore.reset_history()">
reset
</v-btn>
</template>