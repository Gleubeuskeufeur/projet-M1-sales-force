package main

import (
	"net/http"
)

type ImmoCRMServer struct {
	*http.Server
}

func NewImmoCRMServer() (immoCRMServer *ImmoCRMServer, err error) {
	servMux := http.NewServeMux()

	controller, err := NewDemoImmoCRMController()
	if err != nil {
		return
	}

	servMux.HandleFunc("/Lyon", func(w http.ResponseWriter, r *http.Request) {
		data, errCh := controller.GetData(r.Context(), "Lyon")
		select {
		case b := <-data:
			w.Write(b)
		case err := <-errCh:
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
	})
	servMux.HandleFunc("/Lille", func(w http.ResponseWriter, r *http.Request) {
		data, errCh := controller.GetData(r.Context(), "Lille")
		select {
		case b := <-data:
			w.Write(b)
		case err := <-errCh:
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
	})
	servMux.HandleFunc("/Rennes", func(w http.ResponseWriter, r *http.Request) {
		data, errCh := controller.GetData(r.Context(), "Rennes")
		select {
		case b := <-data:
			w.Write(b)
		case err := <-errCh:
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
	})

	server := http.Server{
		Addr:    ":9191",
		Handler: servMux,
	}

	immoCRMServer = &ImmoCRMServer{
		Server: &server,
	}

	return
}

func (is *ImmoCRMServer) Start() (err error) {
	err = is.ListenAndServe()
	return
}
