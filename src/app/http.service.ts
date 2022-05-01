import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
	providedIn: 'root'
})
export class HttpService {

	private url = 'http://127.0.0.1:8000/';
	private query = '';
	constructor(private http: HttpClient) { }

	getOffers(page?: number, subcategory?: string) {
		this.query = this.url + 'offers?';

		if (typeof subcategory !== "undefined") {
			if (typeof page !== "undefined") {
<<<<<<< Updated upstream
				this.query += 'page=' + page.toString() + '&subcategory=' + subcategory;
=======
				this.query += 'page=' + (page as unknown as string) + '&subcategory=' + subcategory;
>>>>>>> Stashed changes
			}
			else {
				this.query += 'subcategory=' + subcategory;
			}
		}
		else if (typeof page !== "undefined") {
<<<<<<< Updated upstream
			this.query += 'page=' + page.toString();
=======
			this.query += 'page=' + (page as unknown as string);
>>>>>>> Stashed changes
		}

		return this.http.get(this.query);
	}

	getCategories() {
		this.query = this.url + 'condensed_categories';
		return this.http.get(this.query);
	}

}
