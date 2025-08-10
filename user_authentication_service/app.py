#!/usr/bin/env python3
"""Flask app exposing auth endpoints (Flask 1.1 compatible)."""

from typing import Any, Optional
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def index() -> Any:
    """Health endpoint."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> Any:
    """Register a user from form data."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "email and password required"}), 400
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route("/sessions", methods=["POST"])
def login() -> Any:
    """Log user in, set session_id cookie, return JSON."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", session_id or "")
    return resp


@app.route("/sessions", methods=["DELETE"])
def logout() -> Any:
    """Log out using session_id cookie."""
    session_id: Optional[str] = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile() -> Any:
    """Return the user profile (email) based on session cookie."""
    session_id: Optional[str] = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email})


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token() -> Any:
    """Generate and return a reset token for an email."""
    email = request.form.get("email")
    if not email:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": token})


@app.route("/reset_password", methods=["PUT"])
def update_password() -> Any:
    """Update password given email, reset_token, and new_password."""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    if not email or not reset_token or not new_password:
        abort(403)
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
