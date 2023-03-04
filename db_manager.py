import pypyodbc

class ServerSQL():
    
    def __init__(self, config):
        self.request = f"""
            DRIVER={{{config['drivers']}}};
            SERVER={config['server']};
            UID={config['user']};
            PWD={config['password']};
            DATABASE={config['database']};
            Trusted_Connection={config['trusted_connection']};
        """
        print(self.request)
        
    def __enter__(self):
        self.conn = pypyodbc.connect(self.request)
        return self.conn
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()
        