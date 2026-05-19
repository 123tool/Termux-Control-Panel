import os
import re
import subprocess
from flask import Flask, jsonify, request, render_template
from command_schema import COMMAND_SCHEMAS

app = Flask(__name__)

def execute_command_safe(cmd_id, user_inputs):
    """
    Lapisan Eksekusi Aman.
    Menghindari shell=True dan melakukan regex validation per argumen.
    """
    if cmd_id not in COMMAND_SCHEMAS:
        return {"status": "error", "message": "Perintah ilegal / tidak terdaftar!"}
    
    schema = COMMAND_SCHEMAS[cmd_id]
    binary = schema["binary"]
    
    # Base command array
    cmd_array = [binary]
    
    # Jalankan validasi masukan user berdasarkan skema regex
    for param in schema["params"]:
        p_name = param["name"]
        val = str(user_inputs.get(p_name, param.get("default", ""))).strip()
        
        # Validasi kecocokan karakter (Anti-Injection)
        if "validation" in param:
            if not re.match(param["validation"], val):
                return {"status": "error", "message": f"Input tidak valid pada parameter: {param['label']}"}
        
        # Aturan penyusunan argumen spesifik Termux-API
        if cmd_id == "torch":
            cmd_array.append(val)
        elif cmd_id == "volume":
            if p_name == "stream":
                cmd_array.extend(["-d", val])
            elif p_name == "volume":
                cmd_array.append(val)
        elif cmd_id == "tts":
            if p_name == "text":
                cmd_array.append(val)
        elif cmd_id == "vibrate":
            if p_name == "duration":
                cmd_array.extend(["-d", val])
            elif p_name == "force" and val == "Ya":
                cmd_array.append("-f")
        elif cmd_id == "location":
            if p_name == "provider":
                cmd_array.extend(["-p", val])
        elif cmd_id == "toast":
            if p_name == "text":
                cmd_array.append(val)
            elif p_name == "color":
                cmd_array.extend(["-b", val])

    try:
        # Eksekusi aman tanpa shell=True
        result = subprocess.run(
            cmd_array, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            timeout=10
        )
        
        if result.returncode == 0:
            output = result.stdout.strip() if result.stdout.strip() else "Perintah berhasil dieksekusi (No Output)."
            return {"status": "success", "output": output}
        else:
            return {"status": "error", "message": result.stderr.strip() or "Terjadi kesalahan internal pada Termux-API."}
            
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Batas waktu eksekusi (Timeout) habis!"}
    except FileNotFoundError:
        return {"status": "error", "message": f"Binary '{binary}' tidak ditemukan! Pastikan termux-api sudah terinstall."}
    except Exception as e:
        return {"status": "error", "message": f"Exception: {str(e)}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/schema', methods=['GET'])
def get_schema():
    """Endpoint untuk Frontend mengambil definisi formulir secara dinamis"""
    return jsonify(COMMAND_SCHEMAS)

@app.route('/api/execute', methods=['POST'])
def execute():
    """Endpoint untuk mengeksekusi perintah secara aman"""
    data = request.json or {}
    cmd_id = data.get("command_id")
    user_inputs = data.get("inputs", {})
    
    if not cmd_id:
        return jsonify({"status": "error", "message": "Missing command_id"}), 400
        
    res = execute_command_safe(cmd_id, user_inputs)
    return jsonify(res)

if __name__ == '__main__':
    # Berjalan lokal di port 5000
    print("====== Termux Remote Control Panel Aktif ======")
    print("Buka browser Android Anda ke: http://127.0.0.1:5000")
    print("===============================================")
    app.run(host='127.0.0.1', port=5000, debug=True)
