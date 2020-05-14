import { TestBed } from '@angular/core/testing';

import { ButtonManagerService } from './button-manager.service';

describe('ButtonManagerService', () => {
  let service: ButtonManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ButtonManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
