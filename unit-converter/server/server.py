from http.server import HTTPServer, SimpleHTTPRequestHandler
import os, json

PORT = 8080

def convertLength(from_unit: str, to_unit: str, value: float) -> float:
    # intermediary unit = meter
    
    if from_unit == to_unit:
        return value
    
    match from_unit:
        case 'mm':
            value *= 0.001
        case 'cm':
            value *= 0.01
        case 'm':
            pass
        case 'km':
            value *= 1000.0
        case 'in':
            value *= 0.0254
        case 'ft':
            value *= 0.3048
        case 'yd':
            value *= 0.9144
        case 'mi':
            value *= 1609.344
        case _:
            raise TypeError(f'Invalid from unit type: {from_unit}')
        
    match to_unit:
        case 'mm':
            value /= 0.001
        case 'cm':
            value /= 0.01
        case 'm':
            pass
        case 'km':
            value /= 1000.0
        case 'in':
            value /= 0.0254
        case 'ft':
            value /= 0.3048
        case 'yd':
            value /= 0.9144
        case 'mi':
            value /= 1609.344
        case _:
            raise TypeError(f'Invalid to unit type: {to_unit}')
        
    return float(value)


def convertWeight(from_unit: str, to_unit: str, value: float) -> float:
    # intermediary unit = gram
    return float(value)


def convertTemperature(from_unit: str, to_unit: str, value: float) -> float:
    # intermediary unit = celsius
    return float(value)


class Handler(SimpleHTTPRequestHandler):
    def _send_json_response(self, data: dict, status_code: int):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json') 
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    
    def _send_error(self, message: str, status_code:int):
        self.send_response(status_code, message)
        self.end_headers()
    
    
    def do_POST(self):
        content_length: int = int(self.headers['Content-Length'])
        post_data: bytes = self.rfile.read(content_length)
        
        answers: dict = json.loads(post_data.decode())
        try:
            value: float = float(answers['value'])
            from_unit: str = answers['from'].lower()
            to_unit: str = answers['to'].lower()
            match answers['type']:
                case 'length':
                    result = convertLength(from_unit, to_unit, value)
                case 'weight':
                    result = convertWeight(from_unit, to_unit, value)
                case 'temperature':
                    result = convertTemperature(from_unit, to_unit, value)
                case _:
                    raise TypeError('Invalid conversion type')
                
            self._send_json_response({'result':result},200)
            
        except json.JSONDecodeError: # the json is not valid
            self._send_error('Invalid JSON format', 400)
        
        except KeyError: # missing a dict key
            self._send_error('Missing crucial information', 400)        
            
        except ValueError as e: # the 'value' is not a number
            self._send_error('Invalid numeric value', 400)
        
        except TypeError as e: # the value for 'type', 'from', 'to' or 'value' is invalid
            self._send_error(str(e), 400)
        
if os.path.exists("../client"):
    os.chdir("../client")
    server = HTTPServer(('localhost', PORT), Handler)
    print(f"http://localhost:{PORT}")
    server.serve_forever()