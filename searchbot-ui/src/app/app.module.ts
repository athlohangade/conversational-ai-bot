import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ChatwindowComponent } from './chatwindow/chatwindow.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { MessageboxComponent } from './messagebox/messagebox.component';
import { ButtonRepliesComponent } from './button-replies/button-replies.component';

@NgModule({
  declarations: [
    AppComponent,
    ChatwindowComponent,
    WelcomeComponent,
    MessageboxComponent,
    ButtonRepliesComponent
  ],
  imports: [
    BrowserModule,
	AppRoutingModule,
	HttpClientModule,
	FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
