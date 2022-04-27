using Fileshare.Domain.Modules;

namespace Fileshare.Contracts.Services
{
    public interface IPConfigurationService 
    {
        int Port { get; }
        Peer<IPingService> Peer { get; }
        bool StartPeerService();
        bool StopPeerService();
    }
}
