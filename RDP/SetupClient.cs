using System;
using System.Net;

namespace 원격제어기
{
    public class RecvRCInfoEventArgs:EventArgs
    {
        public IPEndPoint IPEndPoint
        {
            get;
            private set; 
        }
        public string IPAddressStr
        {
            get 
            {
                return IPEndPoint.Address.ToString(); 
            }
        }
        public int Port
        {
            get 
            {
                return IPEndPoint.Port; 
            }
        }
        internal RecvRCInfoEventArgs(EndPoint RemoteEndPoint)
        {
            IPEndPoint = RemoteEndPoint as IPEndPoint;
        }
    }
    public delegate void RecvRCInfoEventHandler(object sender, RecvRCInfoEventArgs e);
}