def put_settings(es, params):
    es.cluster.put_settings(body=params["body"])


def register(registry):
    # register a fallback for older Benchmark versions
    try:
        from osbenchmark.worker_coordinator.runner import PutSettings
    except ImportError:
        registry.register_runner("put-settings", put_settings)
