# 🔀🔒 Polymorphic Shellcode Engine

> **Maintenance status:** Historical research code from 2025. The examples have not been revalidated against current platforms or dependencies. Current vulnerability research is published in [AI Infrastructure Security](https://github.com/Aviral2642/ai-infra-security); see the [public profile](https://github.com/Aviral2642) for recent work.


A next-generation engine for generating metamorphic shellcode payloads with built-in evasion capabilities, designed for red team operations and penetration testing.

## 🚀 Features

- **Advanced Polymorphism**
  - Runtime code mutation (junk insertion, register swapping)
  - Architecture-aware instruction reordering
  - Context-aware NOP sled generation

- **Stealth & Evasion**
  - XOR encryption with PBKDF2 key derivation
  - Anti-analysis techniques (sandbox detection, VM checks)
  - API hashing for IAT obfuscation

- **Payload Generation**
  - Keystone-engine powered assembler
  - Pre-built templates (reverse TCP, bind shells)
  - Cross-architecture support (x86/x64)

- **Operational Integration**
  - Cobalt Strike `.cna` script generation
  - Raw shellcode output for custom loaders
  - Process injection templates

## 📦 Installation

```bash
git clone https://github.com/Aviral2642/Polymorphic-Shellcode-Engine.git
cd Polymorphic-Shellcode-Engine
pip install -r requirements.txt
