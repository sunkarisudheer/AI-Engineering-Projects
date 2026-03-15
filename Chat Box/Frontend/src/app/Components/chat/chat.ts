import { Component , ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService } from '../../service/chat-service';

@Component({
  selector: 'app-chat',
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.html',
  styleUrl: './chat.css',
})
export class Chat {
   userInput = '';
   isLoading = false;
   messages: { text: string; sender: string }[] = [];
  
    constructor(private chatService: ChatService,
                private cdr: ChangeDetectorRef
    ){}
  
    sendMessage(){
      this.isLoading = true;
      const text =  this.userInput.trim();
      if(!text) return;
  
      this.messages.push({ text, sender : 'user' });
      this.userInput = '';
        
      this.chatService.sendMessage(text).subscribe({
        next: (res) => {
          console.log('Backend response:', res);
          const reply = res?.reply?.trim()?res.reply : 'No response generated.';
          this.messages.push({ text: res.reply, sender: 'bot' });
          this.isLoading = false;
          this.cdr.detectChanges(); // force immediate UI refresh

        },
        error: (err) => {
          console.log('Error:', err);
          this.messages.push({ text : 'something went wrong.', sender: 'bot'});
          this.isLoading = false;
        }
      });
    }
}
