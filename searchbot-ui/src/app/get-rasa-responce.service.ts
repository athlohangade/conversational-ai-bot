import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GetRasaResponceService {

	RASA_URL: string = "/webhooks/rest/webhook";

	constructor(private http: HttpClient) { }

	sendMessage(message: string): Observable<any> {
		var data = {
			"sender": "Me",
			"message": message
		};
		return this.http.post(this.RASA_URL, data)
	}
}
