import { TestBed } from '@angular/core/testing';

import { AllmessagesService } from './allmessages.service';

describe('AllmessagesService', () => {
  let service: AllmessagesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AllmessagesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
