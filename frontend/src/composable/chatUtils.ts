import { useConversationStore } from '@/stores/conversationStore';
import { onMounted, onUnmounted ,computed} from 'vue';


export function chatUtils() {
  const conversationStore = useConversationStore();
  const messages = computed(() => conversationStore.history);
  const lastMessage = computed(() => {
    const arr = messages.value;
    return arr && arr.length ? arr[arr.length - 1] : null;
  });
}