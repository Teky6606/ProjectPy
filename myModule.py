def tim_kiem_phan_tu(ds, so_can_tim):
    for i in range(len(ds)):
        if ds[i] == so_can_tim:
            return i # tôi đã tìm thấy
    return -1 # tôi không tìm thấy