<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
              <div class="space-y-4">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        <p class="text-xs"><strong>Johnson Kaberere</strong></p>
                    </div>

                    <span class="text-xs text-gray-500">18 minutes ago</span>
                </div>
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        <p class="text-xs"><strong>Johnson Kaberere</strong></p>
                    </div>

                    <span class="text-xs text-gray-500">18 minutes ago</span>
                </div>
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        <p class="text-xs"><strong>Johnson Kaberere</strong></p>
                    </div>

                    <span class="text-xs text-gray-500">18 minutes ago</span>
                </div>
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-2">
                        <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">

                        <p class="text-xs"><strong>Johnson Kaberere</strong></p>
                    </div>

                    <span class="text-xs text-gray-500">18 minutes ago</span>
                </div>
              </div>
            </div>
        </div>

        <div class="main-center col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                    <template
                        v-for="message in chatHistory" :key="message.id"
                    >
                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end"
                            v-if="message.type === 'user'"
                        >
                            <div>
                                <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
                                    <p class="text-sm">You: {{ message.text }}</p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">2 min ago</span>
                            </div>
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                            </div>
                        </div>

                        <div 
                            class="flex w-full mt-2 space-x-3 max-w-md"
                            v-else-if="message.type === 'chatbot'"
                        >
                            <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                                <img src="https://i.pravatar.cc/300?img=70" class="w-[40px] rounded-full">
                            </div>
                            <div>
                                <div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
                                    <p class="text-sm" v-html="formatMessageText(message.text)"></p>
                                </div>
                                <span class="text-xs text-gray-500 leading-none">2 min ago</span>
                            </div>
                        </div>

                    </template>

                    
                </div>
            </div>
            <div class="bg-white border border-gray-200 rounded-lg">
               <form v-on:submit.prevent="sendMessage">
                    <div class="p-4">
                        <textarea v-model="userInput" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What message do you want to send?"></textarea>
                    </div>

                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Send</button>
                    </div>
                </form>
           </div>
        </div>
    </div>
  
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            chatHistory: [],
            userInput: '',
        }
    },

    methods: {
        formatMessageText(text) {
            // Replace newlines with HTML line breaks to preserve the formatting
            return text.replace(/\n/g, "<br>");
        },
        
        sendMessage() {
            this.chatHistory.push({id: Date.now(), type: 'user', text: this.userInput});

            axios
                .post('/api/chatbot/', { 'userInput': this.userInput })
                .then(response => {
                    console.log('data', response.data)
                    const chatBotResponse = response.data.response;
                    console.log('chatBotResponse', chatBotResponse)
                    this.chatHistory.push({id: Date.now(), type: 'chatbot', text: chatBotResponse });
                    console.log('ChatHistory', this.chatHistory)
                })
                .catch(error => {
                    console.log('error', error);
                });
        
            this.userInput = '';
        }



    }

}
</script>

<style>

</style>