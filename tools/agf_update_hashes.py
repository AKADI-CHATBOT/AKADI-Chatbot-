#!/usr/bin/env python3
"""SIL oficial - Actualiza hashes de Boot y Kernel, sync TXT, actualiza README."""
import pathlib, hashlib, sys
def sha256_of(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def main():
    root = pathlib.Path(".")
    boot = root / "docs/governance/CHATBOT_BOOT_PROMPT.md"
    kernel = root / "docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md"
    txt = root / "docs/governance/CHATBOT_BOOT_PROMPT.txt"
    readme = root / "README.md"
    boot_hash_f = root / ".boot_hash.sha256"
    kernel_hash_f = root / ".kernel_hash.sha256"
    kernel_hash_gov = root / "docs/governance/.kernel_hash.sha256"
    if not boot.exists() or not kernel.exists() or not readme.exists():
        print("Falta archivo base")
        sys.exit(1)
    old_boot = boot_hash_f.read_text(encoding="utf-8").strip() if boot_hash_f.exists() else ""
    old_kernel = kernel_hash_f.read_text(encoding="utf-8").strip() if kernel_hash_f.exists() else ""
    txt.write_text(boot.read_text(encoding="utf-8"), encoding="utf-8")
    new_boot = sha256_of(boot)
    new_kernel = sha256_of(kernel)
    boot_hash_f.write_text(new_boot + "\n", encoding="utf-8")
    kernel_hash_f.write_text(new_kernel + "\n", encoding="utf-8")
    kernel_hash_gov.write_text(new_kernel + "\n", encoding="utf-8")
    readme_t = readme.read_text(encoding="utf-8")
    if old_boot and old_boot in readme_t:
        readme_t = readme_t.replace(old_boot, new_boot)
    else:
        print("AVISO: old boot no en README, no se reemplazo hash boot")
    if old_kernel and old_kernel in readme_t:
        readme_t = readme_t.replace(old_kernel, new_kernel)
    else:
        print("AVISO: old kernel no en README")
    readme.write_text(readme_t, encoding="utf-8")
    print(f"NEW_BOOT={new_boot}")
    print(f"NEW_KERNEL={new_kernel}")
    print("Hashes actualizados y TXT sincronizado")
if __name__ == "__main__":
    main()
