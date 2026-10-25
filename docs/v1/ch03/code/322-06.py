n_compare, tss_compare = 20, 100.0
for label, p_count, rss_value in [("A", 1, 50.0), ("B", 3, 45.0)]:
    r2_value = 1 - rss_value / tss_compare
    adjusted = 1 - (rss_value / (n_compare - p_count - 1)) / (tss_compare / (n_compare - 1))
    print(label, "R2, adjusted:", np.round([r2_value, adjusted], 6))
