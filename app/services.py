from flask import Flask, jsonify, request

@app.route("/api/notes", methods=["POST"])
def create_note():
    new_note = {
        "id": len(notes) + 1,
        "title": request.json.get("title"),
        "content": request.json.get("content"),
        "created_at": request.json.get("created_at"),
    }
    notes.append(new_note)
    return jsonify({"message": "Note created successfully", "note": new_note}), 400


@app.route("/api/notes", methods=["GET"])
def get_all_notes():
    return jsonify({"notes": notes})


@app.route("/api/notes/<int:note_id>", methods=["GET"])
def get_single_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    if not note:
        return jsonify({"message": "Note not found"}), 400
    return jsonify({"note": note})


@app.route("/api/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = [note for note in notes if note["id"] == note_id]
    if not note:
        return jsonify({"message": "Note not found"}), 400
    note[0]["title"] = request.json.get("title", note[0]["title"])
    note[0]["content"] = request.json.get("content", note[0]["content"])
    return jsonify({"message": "Note updated successfully", "note": note[0]})


@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_book(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return jsonify({"message": "Note deleted successfully"})
