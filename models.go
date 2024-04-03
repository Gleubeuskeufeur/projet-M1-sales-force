package main

type RealEstateRecord struct {
	IDParcelle         string `json:"id_parcelle"`
	DateMutation       string `json:"date_mutation"`
	ValeurFonciere     string `json:"valeur_fonciere"`
	SurfaceReelle_bati string `json:"surface_reelle_bati"`
	SurfaceTerrain     string `json:"surface_terrain"`
	Date1              string `json:"date1"`
}
