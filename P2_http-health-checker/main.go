package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"time"
)

// Config representa la estructura del archivo de configuración.
type Config struct {
	Services             []Service `json:"services"`
	CheckIntervalSeconds int       `json:"check_interval_seconds"`
	TimeoutSeconds       int       `json:"timeout_seconds"`
}

// Service define un servicio a monitorear.
type Service struct {
	Name     string `json:"name"`
	URL      string `json:"url"`
	Method   string `json:"method"`
	Expected int    `json:"expected_status"`
}

// checkService realiza una petición HTTP y comprueba el código de respuesta.
func checkService(service Service, timeout time.Duration) (bool, error) {
	client := http.Client{
		Timeout: timeout,
	}

	req, err := http.NewRequest(service.Method, service.URL, nil)
	if err != nil {
		return false, err
	}

	resp, err := client.Do(req)
	if err != nil {
		return false, err
	}
	defer resp.Body.Close()

	if resp.StatusCode == service.Expected {
		return true, nil
	}
	return false, fmt.Errorf("código %d, esperado %d", resp.StatusCode, service.Expected)
}

func loadConfig(path string) (Config, error) {
	var config Config
	file, err := os.Open(path)
	if err != nil {
		return config, err
	}
	defer file.Close()

	bytes, err := ioutil.ReadAll(file)
	if err != nil {
		return config, err
	}

	err = json.Unmarshal(bytes, &config)
	return config, err
}

func main() {
	config, err := loadConfig("config.json")
	if err != nil {
		log.Fatalf("No se pudo cargar la configuración: %v", err)
	}

	timeout := time.Duration(config.TimeoutSeconds) * time.Second
	ticker := time.NewTicker(time.Duration(config.CheckIntervalSeconds) * time.Second)

	for {
		select {
		case <-ticker.C:
			for _, service := range config.Services {
				ok, err := checkService(service, timeout)
				if ok {
					log.Printf("[OK] %s (%s) responde correctamente.", service.Name, service.URL)
				} else {
					log.Printf("[ERROR] %s (%s) falló: %v", service.Name, service.URL, err)
				}
			}
		}
	}
}
