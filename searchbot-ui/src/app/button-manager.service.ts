import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ButtonManagerService {

	private isButtonActivated: boolean = false;

	btn: any[] = null;

	public hasButtons(): boolean {
		return this.isButtonActivated;
	}

	public activateButton(btn: any[]): void {
		this.isButtonActivated = true;
		this.btn = btn;
	}

	public deactivateButton(): void {
		this.isButtonActivated = false;
	}

	constructor() { }
}
