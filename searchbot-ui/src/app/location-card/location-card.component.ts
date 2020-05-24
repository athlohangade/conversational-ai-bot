import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-location-card',
  templateUrl: './location-card.component.html',
  styleUrls: ['./location-card.component.css']
})
export class LocationCardComponent implements OnInit {

  @Input() cards: any[];

  constructor() { }

  ngOnInit(): void {
  }

}
