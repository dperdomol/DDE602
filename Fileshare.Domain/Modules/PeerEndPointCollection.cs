using System.Net;
using System.Net.PeerToPeer;

namespace Fileshare.Domain.Modules
{
    public class PeerEndPointsCollection 
    {

        public PeerEndPointsCollection(PeerName peer, IPEndPointCollection iPEndpoint)
        {
            PeerHostName = peer;
            PeerEndPoints = iPEndpoint;
        }

        public PeerName PeerHostName { get; }
        public IPEndPointCollection PeerEndPoints { get; }

    }
}
