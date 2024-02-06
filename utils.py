from datetime import datetime, timedelta
from models import db, UserRequest

exempted_ips = ['127.0.0.1']
def check_user_request_limit(ip_address):
    user_request = UserRequest.query.filter_by(ip_address=ip_address).first()
    if ip_address in exempted_ips:
        # IP exenta, no aplicar restricciones
        return True

    if user_request:
        # Verifica si ha pasado un día desde la última solicitud
        if datetime.utcnow() - user_request.last_request_date >= timedelta(days=1):
            # Reinicia el conteo de solicitudes y actualiza la fecha
            user_request.request_count = 1
            user_request.last_request_date = datetime.utcnow()
        else:
            # Verifica si se ha alcanzado el límite de solicitudes
            if user_request.request_count >= 3:
                print(f"Número máximo de solicitudes alcanzado para la IP {user_request.ip_address}. Conteo: {user_request.request_count}")
                return False
            # Incrementa el conteo de solicitudes
            user_request.request_count += 1
    else:
        # Crea una nueva entrada para el usuario
        new_user_request = UserRequest(ip_address=ip_address, request_count=1)
        db.session.add(new_user_request)

    db.session.commit()
    return True
