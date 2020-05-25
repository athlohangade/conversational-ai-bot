import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AtmLocationCardsService {

	private cards: any[] = [];

	public pushLocation(location: any): void {
		this.cards.push(location);
	}

	public hasLocationsLeft(): boolean {
		return this.cards.length > 0;
	}

	public pop4(): any[] {
		var locations: any[] = [];
		var i: number;
		for(i = 0; i < 4; i++) {
			locations.push(this.cards.shift());
			if(this.cards.length == 0)
                break;
		}
		return locations;
	}

	public emptyLocations(): void {
		this.cards = [];
	}

	constructor() { }
}
