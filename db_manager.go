package main

import (
	"database/sql"
	"encoding/json"
	"fmt"

	_ "modernc.org/sqlite"
)

type ImmoCRMDBManager interface {
	FetchImmoData(city string) (chan []byte, chan error)
}

type SQLImmoCRMDBManager struct {
	*sql.DB
}

func NewSQLImmoCRMDBManager() (manager *SQLImmoCRMDBManager, err error) {
	db, err := sql.Open("sqlite", "./bases_de_donnees/Ma_Base_De_Donnees_v2.db")
	if err != nil {
		return
	}
	manager = &SQLImmoCRMDBManager{
		DB: db,
	}
	return
}

func (idbm *SQLImmoCRMDBManager) FetchImmoData(city string) (data chan []byte, errCh chan error) {
	data, errCh = make(chan []byte), make(chan error)
	go func() {
		stats := idbm.DB.Stats()
		fmt.Println("nbr of connections", stats.InUse)
		rows, err := idbm.Query(fmt.Sprintf("SELECT id_parcelle,date_mutation,valeur_fonciere,surface_reelle_bati,surface_terrain,Date_1 FROM %s", city))
		if err != nil {
			errCh <- err
			return
		}
		// defer idbm.Close()
		records := []*RealEstateRecord{}
		for rows.Next() {
			var idParcelle string
			var dateMutation string
			var valeurFonciere string
			var surfaceReelleBati string
			var surfaceTerrain string
			var date1 string

			if err = rows.Scan(&idParcelle, &dateMutation, &valeurFonciere, &surfaceReelleBati, &surfaceTerrain, &date1); err != nil {
				errCh <- err
				return
			}

			record := RealEstateRecord{
				IDParcelle:         idParcelle,
				DateMutation:       dateMutation,
				ValeurFonciere:     valeurFonciere,
				SurfaceReelle_bati: surfaceReelleBati,
				SurfaceTerrain:     surfaceTerrain,
				Date1:              date1,
			}

			records = append(records, &record)
		}
		bs, err := json.Marshal(&records)
		if err != nil {
			errCh <- err
			return
		}
		data <- bs
	}()

	return
}
