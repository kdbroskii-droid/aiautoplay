from storage.json_store import JsonStore


def test_json_store_round_trip(tmp_path) -> None:
    store = JsonStore(tmp_path)
    store.save("state", {"score": 3})
    assert store.load("state") == {"score": 3}
