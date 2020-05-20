import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GetRasaResponceService {

	RASA_URL: string = "/webhooks/rest/webhook";
	USERNAME: string;

	constructor(private http: HttpClient) {
		var d: Date = new Date();
		var randomNum: number = Math.round(Math.random() * 1000);
		var name: string = `user#${randomNum}:${d.getUTCHours()}:${d.getUTCMinutes()}:${d.getUTCSeconds()}:${d.getUTCMilliseconds()}`;
		this.USERNAME = name;
		console.log(`username: ${this.USERNAME}`);
	}

	sendMessage(message: string): Observable<any> {
		var data = {
			"sender": this.USERNAME,
			"message": message
		};
		return this.http.post(this.RASA_URL, data)
	}
}
