def format_solution(title, path, execution_time):
    lines = [
        f"Tower of Hanoi - {title}",
        "=" * 40,
    ]

    if path is None:
        lines.append("Solusi tidak ditemukan.")
        lines.append("")
        lines.append("Jumlah perpindahan: tidak tersedia")
        return "\n".join(lines) + "\n"

    lines.append(f"Jumlah state: {len(path)}")
    lines.append(f"Jumlah perpindahan: {len(path) - 1}")
    lines.append("")
    lines.append(f"Waktu pengalkulasian: {execution_time:.9f} detik")

    for step, state in enumerate(path):
        pegs = {"A": [], "B": [], "C": []}

        for disk, peg_index in enumerate(state):
            peg_name = "ABC"[peg_index]
            # Simpan label cakram
            pegs[peg_name].append(disk + 1)

        # Tampilkan cakram dari bawah ke atas.
        for peg in pegs:
            pegs[peg].sort(reverse=True)

        lines.append(
            f"State {step}: "
            f"A={pegs['A']} | B={pegs['B']} | C={pegs['C']}"
        )

        if step < len(path) - 1:
            current = state
            nxt = path[step + 1]
            moved_disk = next(
                i for i, (a, b) in enumerate(zip(current, nxt)) if a != b
            )
            source = "ABC"[current[moved_disk]]
            target = "ABC"[nxt[moved_disk]]
            lines.append(
                f"  Langkah {step + 1}: pindahkan cakram "
                f"{moved_disk + 1} dari {source} ke {target}"
            )

    return "\n".join(lines) + "\n"
