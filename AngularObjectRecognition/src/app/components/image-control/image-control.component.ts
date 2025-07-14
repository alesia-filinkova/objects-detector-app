import { Component } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-image-control',
  standalone: true,
  imports: [],
  templateUrl: './image-control.component.html',
  styleUrl: './image-control.component.css'
})
export class ImageControlComponent {
  imageUrl: string | null = null;
  selectedFile: File | null = null;
  // prediction$: Observable<any[] | null>;
  // loading$: Observable<boolean>;
  // error$: Observable<string | null>;
}
