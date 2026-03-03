<script setup>
import { useRouter } from 'vue-router';
import { useConversationStore } from '@/stores/conversationStore';
const conversationStore = useConversationStore();
const router = useRouter();

const new_room = async () => {
    conversationStore.getRoomType()
    if (conversationStore.roomType==="Chatroom"){
        router.push("/game")
    }
    else if (conversationStore.roomType==="Cinematic"){
        router.push("/cinematic")
    }

}
</script>
<template>
    <v-btn color="secondary" prepend-icon="mdi-check-all" @click="new_room">
        Prochaine room
    </v-btn>
</template>