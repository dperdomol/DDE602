using Fileshare.Domain.Modules;
using System.Net.PeerToPeer.Collaboration;

namespace Fileshare.Contracts.Repository
{
    public interface IPeerNameResolverRepository
    {
        void ResolvePeerName();
        PeerEndPointsCollection PeerEndPointCollection { get; set; }
    }
}
