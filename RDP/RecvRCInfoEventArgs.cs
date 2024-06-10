using System.Net.Sockets;
using System.Threading;
using System.Net;

namespace 원격제어기
{
    public static class SetupServer
    {
        static Socket lis_sock;
        static Thread accept_thread = null;
        static public event RecvRCInfoEventHandler RecvedRCInfo = null;

        static public void Start(string ip, int port)
        {
            IPAddress ipaddr = IPAddress.Parse(ip);
            IPEndPoint ep = new IPEndPoint(ipaddr, port);
            lis_sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream,
                                         ProtocolType.Tcp);
            lis_sock.Bind(ep);
            lis_sock.Listen(1);
            ThreadStart ts = new ThreadStart(AcceptLoop);
            accept_thread = new Thread(ts);
            accept_thread.Start();
        }

        static void AcceptLoop()
        {
            try
            {
                while (true)
                {
                    Socket do_sock = lis_sock.Accept();
                    if (RecvedRCInfo != null)
                    {
                        RecvRCInfoEventArgs e = new RecvRCInfoEventArgs(
                                                          do_sock.RemoteEndPoint);
                        RecvedRCInfo(null, e);
                    }
                    do_sock.Close();
                }
            }
            catch 
            {
                Close();
            }
        }
        public static void Close()
        {
            if (accept_thread != null)
            {
                accept_thread = null;
            }
            if (lis_sock != null)
            {
                lis_sock.Close();
                lis_sock = null;
            }
        }
    }
}