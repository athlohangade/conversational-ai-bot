import { TestBed } from '@angular/core/testing';

import { GetRasaResponceService } from './get-rasa-responce.service';

describe('GetRasaResponceService', () => {
  let service: GetRasaResponceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetRasaResponceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
