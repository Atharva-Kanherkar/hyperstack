
def summarize(records):
    results = {}

    # Group records by class
    groups = defaultdict(list)
    for record in records:
        groups[record["class"]].append(record)

    for cls, requests in groups.items():
        count = len(requests)
        failures = sum(not r["ok"] for r in requests)

        ttfts = []
        all_itls_ms = []
        attained = 0

        for r in requests:
            if not r["ok"]:
                continue

            # TTFT (seconds)
            ttft = r["t_first"] - r["t_send"]
            ttfts.append(ttft)

            # ITL (milliseconds)
            chunks = r["t_chunks"]
            itls_ms = []

            for i in range(1, len(chunks)):
                gap = (chunks[i] - chunks[i - 1]) * 1000
                itls_ms.append(gap)
                all_itls_ms.append(gap)

            # Mean TPOT (milliseconds)
            if len(itls_ms) > 0:
                mean_tpot = sum(itls_ms) / len(itls_ms)
            else:
                mean_tpot = None  # Single token

            # SLO attainment
            ttft_ok = ttft <= 2.0
            tpot_ok = mean_tpot is None or mean_tpot <= 50

            if ttft_ok and tpot_ok:
                attained += 1

        # Store summary for this class
        results[cls] = {
            "count": count,
            "failures": failures,
            "attainment": attained / count if count else 0,
            "p50_ttft": nearest_rank(ttfts, 0.50),
            "p99_ttft": nearest_rank(ttfts, 0.99),
            "p99_itl": nearest_rank(all_itls_ms, 0.99),
        }

    return results
