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
				this.query += 'page=' + (page as string) + '&subcategory=' + subcategory;
			}
			else {
				this.query += 'subcategory=' + subcategory;
			}
		}
		else if (typeof page !== "undefined") {
			this.query += 'page=' + (page as string);
		}

		return this.http.get(this.query);
	}

	getCategories() {
		this.query = this.url + 'condensed_categories';
		return this.http.get(this.query);
	}

}
