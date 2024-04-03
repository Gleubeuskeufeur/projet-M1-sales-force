package main

import "context"

type ImmoCRMController interface {
	GetData(ctx context.Context, city string) (chan []byte, chan error)
}

type DemoImmoCRMController struct {
	DBManager ImmoCRMDBManager
}

func NewDemoImmoCRMController() (demoImmoCRMController *DemoImmoCRMController, err error) {
	dbManager, err := NewSQLImmoCRMDBManager()
	if err != nil {
		return
	}

	demoImmoCRMController = &DemoImmoCRMController{
		DBManager: dbManager,
	}
	return
}

func (dc *DemoImmoCRMController) GetData(ctx context.Context, city string) (data chan []byte, errCh chan error) {
	data, errCh = make(chan []byte), make(chan error)
	go func() {
		d, e := dc.DBManager.FetchImmoData(city)
		select {
		case result := <-d:
			data <- result
		case err := <-e:
			errCh <- err
		case <-ctx.Done():
			errCh <- ctx.Err()
		}
	}()
	return
}
