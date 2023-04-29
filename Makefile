build:
	docker compose build

run:
	docker compose run --rm video-editor

edit:
	docker compose run --rm video-editor $(input) $(output)

clean:
	docker compose down

.PHONY: build run edit clean

