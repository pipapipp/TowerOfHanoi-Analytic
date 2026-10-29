from pathlib import Path
from algorithms import dfs, dls, ids
import time

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

def read_config(path):
    config = {
        "disks": 3,
        "pegs": 3,
        "methods": ["dfs"],
        "dls_limit": 7,
        "initial_peg": 1,  
        "goal_peg": None, 
    }

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line or "=" not in line:
            continue
        key, value = (part.strip() for part in line.split("=", 1))
        key = key.lower()
        
        if key == "disks":
            config["disks"] = int(value)
        elif key == "methods":
            config["methods"] = [
                method.strip().lower()
                for method in value.split(",")
                if method.strip()
            ]
        elif key == "dls_limit":
            config["dls_limit"] = int(value)
        elif key == "pegs":
            config["pegs"] = int(value)
        elif key == "initial_peg":
            config["initial_peg"] = int(value)
        elif key == "goal_peg":
            config["goal_peg"] = int(value)

    if config["disks"] < 1:
        raise ValueError("'disks' harus minimal 1.")
    if config["goal_peg"] is None:
        config["goal_peg"] = config["pegs"]
    valid_methods = {"dfs", "dls", "ids"}
    unknown = set(config["methods"]) - valid_methods
    if unknown:
        raise ValueError(f"Metode tidak dikenal: {', '.join(sorted(unknown))}")
    if not config["methods"]:
        raise ValueError("'methods' harus berisi minimal satu metode.")
    if config["dls_limit"] < 0:
        raise ValueError("'dls_limit' tidak boleh negatif.")
    if config["pegs"] < 3:
        raise ValueError("'pegs' harus minimal 3.")
    if config["pegs"] > 26:
        raise ValueError("'pegs' maksimal 26 (A-Z).")
    if not (1 <= config["initial_peg"] <= config["pegs"]):
        raise ValueError(f"'initial_peg' harus antara 1 dan {config['pegs']}.")
    if not (1 <= config["goal_peg"] <= config["pegs"]):
        raise ValueError(f"'goal_peg' harus antara 1 dan {config['pegs']}.")
    return config

def format_result(input_name, disks, method, result, execution_time):
    lines = [
        f"Input file : {input_name}",
        f"Jumlah disk: {disks}",
        f"Metode     : {method.upper()}",
        f"Waktu eksekusi: {execution_time:.9f} detik",
        "",
    ]
    peg_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if result is None:
        lines.append("Solusi tidak ditemukan dengan batas pencarian yang digunakan.")
    else:
        moves = result
        lines.append(f"Jumlah langkah: {len(moves)}")
        lines.append("")
        if not moves:
            lines.append("Tidak ada langkah yang diperlukan.")
        else:
            for number, (disk, source, destination) in enumerate(moves, start=1):
                source_name = peg_names[source - 1]
                destination_name = peg_names[destination - 1]

                lines.append(
                    f"{number}. Pindahkan disk {disk} dari tiang {source_name} ke tiang {destination_name}"
                )
    return "\n".join(lines) + "\n"

def main():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    input_files = sorted(
        path for path in INPUT_DIR.iterdir()
        if path.is_file() and path.suffix.lower() == ".txt"
    )

    if not input_files:
        print(f"Tidak ada file .txt di folder: {INPUT_DIR}")
        print("Tambahkan satu atau lebih file input .txt, lalu jalankan kembali.")
        return

    processed = 0
    for input_path in input_files:
        try:
            config = read_config(input_path)
        except (OSError, ValueError) as error:
            print(f"[GAGAL] {input_path.name}: {error}")
            continue

        print(f"\nMemproses {input_path.name}...")
        for method in config["methods"]:
            start_time = time.perf_counter()

            inititial_p = config["initial_peg"] - 1
            goal_p = config["goal_peg"] - 1

            if method == "dfs":
                result = dfs(config["disks"], config["pegs"], inititial_p, goal_p)
            elif method == "dls":
                result = dls(config["disks"], config["dls_limit"], config["pegs"], inititial_p, goal_p)
            else:
                result = ids(config["disks"], config["pegs"], inititial_p, goal_p)

            execution_time = time.perf_counter() - start_time

            output_name = f"{input_path.stem}_{method}_output.txt"
            output_path = OUTPUT_DIR / output_name
            output_path.write_text(
                format_result(input_path.name, config["disks"], method, result, execution_time),
                encoding="utf-8",
            )
            print(f"  [{method.upper()}] -> output/{output_name}")
            processed += 1
        

    print(f"\nSelesai. Total hasil dibuat: {processed}")

if __name__ == "__main__":
    main()
