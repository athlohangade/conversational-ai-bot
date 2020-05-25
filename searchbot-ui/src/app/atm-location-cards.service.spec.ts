import { TestBed } from '@angular/core/testing';

import { AtmLocationCardsService } from './atm-location-cards.service';

describe('AtmLocationCardsService', () => {
  let service: AtmLocationCardsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AtmLocationCardsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
